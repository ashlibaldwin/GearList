from rest_framework import serializers
from models import List, Item, User

class ListSerializer(serializers.ModelSerializer):
	def validate_parent(self, value):
		print(self.context['request'].user)
		return value

	#user = serializers.ReadOnlyField(source='user.username')

	class Meta:
		model = List
		fields = ('id', 'title', 'user')

class ItemSerializer(serializers.ModelSerializer):
	todo_list = serializers.PrimaryKeyRelatedField(many=False, queryset=List.objects.all())
	class Meta:
		model = Item
		fields = ('id', 'title', 'todo_list', 'is_completed')

class UserSerializer(serializers.ModelSerializer):
	lists = serializers.PrimaryKeyRelatedField(many=True, queryset=List.objects.all())

	class Meta:
		model = User
		fields = ('id', 'username', 'lists')