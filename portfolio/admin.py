from django.contrib import admin

from .models import Category, Portfolio  # importando Models


# primeira maneira de registrar uma model no admin
class CategoryAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)

# Segunda maneira de registrar uma model no admin
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    ...