from rest_framework import serializers
from apps.pills.search_uploads.models import UploadRequest

class UploadRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadRequest
        fields = ["id", "filename", "url", "status", "created_at", "completed_at", "item_seq"]
        read_only_fields = fields

class UploadRequestCreateSerializer(serializers.Serializer):
    file = serializers.FileField()

    def validate_file(self, value):
        # 파일 객체가 없거나 잘못된 경우
        if not value or not hasattr(value, "size"):
            raise serializers.ValidationError("유효한 파일이 제출되지 않았습니다.")

        max_size = self.context.get("max_upload_size")
        if max_size and value.size > max_size:
            readable_size = f"{value.size / (1024 * 1024):.2f}MB"
            limit_size = f"{max_size / (1024 * 1024):.2f}MB"
            raise serializers.ValidationError(
                f"파일 크기 초과: {readable_size} > 허용 {limit_size}"
            )

        return value