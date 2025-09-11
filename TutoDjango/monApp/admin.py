from decimal import ROUND_HALF_UP, Decimal
from django.contrib import admin
from .models import Categorie, Contenir, Produit, Rayon, Statut

class ProduitFilter(admin.SimpleListFilter):
    title = "filtre produit"
    parameter_name = "custom status"

    def lookups(self, request, model_admin):
        return (
            ("Online", "En ligne"),
            ("Offline", "Hors ligne"),
        )
    
    def queryset(self, request, queryset):
        if self.value() == "Online":
            return queryset.filter(status=1)
        elif self.value() == "Offline":
            return queryset.filter(status=0)
        

def set_Produit_online(modeladmin, request, queryset):
    queryset.update(status=1)
set_Produit_online.short_description = "Mettre en ligne"

def set_Produit_offline(modeladmin, request, queryset):
    queryset.update(status=0)
set_Produit_offline.short_description = "Mettre hors ligne"

class ProduitAdmin(admin.ModelAdmin):
    model = Produit
    list_display = ["refProd", "intituleProd", "prixUnitaireProd", "prixTTCProd", "dateFabrication", "categorie", "status"]
    list_editable = ["intituleProd", "prixUnitaireProd", "dateFabrication"]
    radio_fields = {"status": admin.VERTICAL}
    search_fields = ("intituleProd", "dateFabrication")
    list_filter = (ProduitFilter,)
    date_hierarchy = "dateFabrication"
    ordering = ("-dateFabrication",)
    actions = [set_Produit_online, set_Produit_offline]

    def prixTTCProd(self, instance):
        return (instance.prixUnitaireProd * Decimal("1.20").quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
    
    prixTTCProd.short_description = "Prix TTC"
    prixTTCProd.admin_order_field = "prixUnitaireProd"

class ProduitInline(admin.TabularInline):
    model = Produit
    extra = 1

class CategorieAdmin(admin.ModelAdmin):
    model = Categorie
    inlines = [ProduitInline]

admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Statut)
admin.site.register(Rayon)
admin.site.register(Contenir)
admin.site.register(Produit, ProduitAdmin)