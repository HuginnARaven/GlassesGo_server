from rest_framework import serializers

from glasses.models import Frame, MaterialColor, Material, Lens, LensColor


class MaterialColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialColor
        fields = "__all__"


class MaterialSerializer(serializers.ModelSerializer):
    material_colors = MaterialColorSerializer(read_only=True,
                                              many=True,
                                              source="material_color")

    class Meta:
        model = Material
        fields = [
            "id",
            "name",
            "price",
            "frame",
            "material_colors",
        ]


class LensColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = LensColor
        fields = "__all__"


class LensSerializer(serializers.ModelSerializer):
    lens_colors = LensColorSerializer(read_only=True,
                                      many=True,
                                      source="lens_color")

    class Meta:
        model = Lens
        fields = [
            "id",
            "name",
            "price",
            "frame",
            "lens_colors",
        ]


class FrameSerializer(serializers.ModelSerializer):
    frame_materials = MaterialSerializer(read_only=True,
                                         many=True,
                                         source="frame_material")
    frame_lenses = LensSerializer(read_only=True,
                                  many=True,
                                  source="frame_lens")

    class Meta:
        model = Frame
        fields = [
            "id",
            "name",
            "price",
            "photo_url",
            "frame_materials",
            "frame_lenses",
        ]

