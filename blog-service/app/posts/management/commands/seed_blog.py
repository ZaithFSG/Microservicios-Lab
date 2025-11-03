from django.core.management.base import BaseCommand
from django.utils import timezone
from posts.models import Post
from authors.models import Author
from categories.models import Category
import random
from datetime import timedelta

class Command(BaseCommand):
    help = 'Seeds the database with sample data'

    def handle(self, *args, **kwargs):
        # Limpiar datos existentes
        self.stdout.write('Limpiando datos existentes...')
        Post.objects.all().delete()
        Author.objects.all().delete()
        Category.objects.all().delete()
        
        # Crear 5 categorías de ejemplo
        categories = [
            Category.objects.create(name="Tecnología"),
            Category.objects.create(name="Ciencia"),
            Category.objects.create(name="Programación"),
            Category.objects.create(name="Django"),
            Category.objects.create(name="Inteligencia Artificial"),
        ]
        self.stdout.write(f'Se crearon {len(categories)} categorías.')

        # Crear 3 autores de ejemplo
        authors = [
            Author.objects.create(
                display_name="Juan Pérez",
                email="juan.perez@example.com"
            ),
            Author.objects.create(
                display_name="María García",
                email="maria.garcia@example.com"
            ),
            Author.objects.create(
                display_name="Carlos Rodríguez",
                email="carlos.rodriguez@example.com"
            ),
        ]
        self.stdout.write(f'Se crearon {len(authors)} autores.')

        # Contenido de ejemplo para los posts
        titles = [
            "Introducción a la Inteligencia Artificial",
            "El futuro del desarrollo web",
            "Mejores prácticas en Django",
            "Machine Learning en la práctica",
            "Cómo empezar en la programación",
            "Python vs JavaScript",
            "Arquitectura de microservicios",
            "Desarrollo web moderno",
            "Bases de datos NoSQL",
            "APIs RESTful y GraphQL"
        ]
        
        bodies = [
            "La inteligencia artificial está revolucionando la forma en que interactuamos con la tecnología...",
            "El desarrollo web está en constante evolución, con nuevas tecnologías emergiendo...",
            "Django es un framework robusto que permite desarrollar aplicaciones web de manera eficiente...",
            "El machine learning está transformando diversos sectores de la industria...",
            "Para comenzar en programación, es importante entender los conceptos básicos...",
            "La elección entre Python y JavaScript depende de varios factores...",
            "Los microservicios ofrecen una forma escalable de desarrollar aplicaciones...",
            "Las tecnologías web modernas permiten crear experiencias de usuario excepcionales...",
            "Las bases de datos NoSQL ofrecen flexibilidad para diferentes tipos de datos...",
            "La elección entre REST y GraphQL depende de las necesidades del proyecto..."
        ]

        # Crear 30 posts variados
        for i in range(30):
            # Seleccionar título y cuerpo al azar
            title = random.choice(titles) + f" - Parte {i+1}"
            body = random.choice(bodies)
            
            # Determinar el estado (70% published, 30% draft)
            status = "published" if random.random() < 0.7 else "draft"
            
            # Calcular fecha de publicación (solo si está publicado)
            published_at = timezone.now() - timedelta(days=random.randint(0, 30)) if status == "published" else None
            
            Post.objects.create(
                title=title,
                body=body,
                author=random.choice(authors),
                category=random.choice(categories),
                status=status,
                published_at=published_at,
                views=random.randint(0, 1000) if status == "published" else 0
            )
        
        # Contar posts por estado
        total_posts = Post.objects.count()
        published_posts = Post.objects.filter(status="published").count()
        draft_posts = Post.objects.filter(status="draft").count()
        
        self.stdout.write(self.style.SUCCESS(f'''
Resumen de datos creados:
- Total de categorías: {len(categories)}
- Total de autores: {len(authors)}
- Total de posts: {total_posts}
  * Publicados: {published_posts}
  * Borradores: {draft_posts}
'''))
