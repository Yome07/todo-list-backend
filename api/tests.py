from django.test import TestCase
from rest_framework.test import APITestCase

from api.models import Category


class CategoryModelTests(TestCase):
    def test_category_name_is_used_as_string_representation(self):
        category = Category.objects.create(name="Courses")

        self.assertEqual(str(category), "Course")


class ApiTests(APITestCase):
    def test_health_check_returns_success_status(self):
        response = self.client.get("/health/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

    def test_category_can_be_created_and_name_is_trimmed(self):
        response = self.client.post(
            "/api/categories/",
            {"name": "  Courses  "},
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["name"], "Courses")
        self.assertTrue(Category.objects.filter(name="Courses").exists())

    def test_duplicate_category_is_rejected(self):
        Category.objects.create(name="Courses")

        response = self.client.post(
            "/api/categories/",
            {"name": "Courses"},
            format="json",
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("name", response.data)

    def test_task_can_be_created_and_listed(self):
        category = Category.objects.create(name="Courses")

        create_response = self.client.post(
            "/api/tasks/",
            {"description": " Acheter du pain ", "category_id": category.id},
            format="json",
        )

        self.assertEqual(create_response.status_code, 201)
        self.assertEqual(create_response.data["description"], "Acheter du pain")
        self.assertFalse(create_response.data["is_completed"])
        self.assertEqual(create_response.data["category"]["id"], category.id)

        list_response = self.client.get("/api/tasks/")

        self.assertEqual(list_response.status_code, 200)
        self.assertEqual(len(list_response.data), 1)
        self.assertEqual(list_response.data[0]["description"], "Acheter du pain")
