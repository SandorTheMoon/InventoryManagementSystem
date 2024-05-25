# routers.py

class MeatsRouter:
    route_app_labels = {'inventoryapp'}

    def db_for_read(self, model, **hints):
        if model._meta.model_name == 'meats':
            return 'meats_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.model_name == 'meats':
            return 'meats_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.model_name == 'meats' or obj2._meta.model_name == 'meats':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == 'meats':
            return db == 'meats_db'
        return None

class BakedRouter:
    route_app_labels = {'inventoryapp'}

    def db_for_read(self, model, **hints):
        if model._meta.model_name == 'baked':
            return 'baked_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.model_name == 'baked':
            return 'baked_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.model_name == 'baked' or obj2._meta.model_name == 'baked':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == 'baked':
            return db == 'baked_db'
        return None

class DairyRouter:
    route_app_labels = {'inventoryapp'}

    def db_for_read(self, model, **hints):
        if model._meta.model_name == 'dairy':
            return 'dairy_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.model_name == 'dairy':
            return 'dairy_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.model_name == 'dairy' or obj2._meta.model_name == 'dairy':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == 'dairy':
            return db == 'dairy_db'
        return None

class PlantsRouter:
    route_app_labels = {'inventoryapp'}

    def db_for_read(self, model, **hints):
        if model._meta.model_name == 'plants':
            return 'plants_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.model_name == 'plants':
            return 'plants_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.model_name == 'plants' or obj2._meta.model_name == 'plants':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == 'plants':
            return db == 'plants_db'
        return None

class CondimentsRouter:
    route_app_labels = {'inventoryapp'}

    def db_for_read(self, model, **hints):
        if model._meta.model_name == 'condiments':
            return 'condiments_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.model_name == 'condiments':
            return 'condiments_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.model_name == 'condiments' or obj2._meta.model_name == 'condiments':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == 'condiments':
            return db == 'condiments_db'
        return None

class BeveragesRouter:
    route_app_labels = {'inventoryapp'}

    def db_for_read(self, model, **hints):
        if model._meta.model_name == 'beverages':
            return 'beverages_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.model_name == 'beverages':
            return 'beverages_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.model_name == 'beverages' or obj2._meta.model_name == 'beverages':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == 'beverages':
            return db == 'beverages_db'
        return None
    
class DryRouter:
    route_app_labels = {'inventoryapp'}

    def db_for_read(self, model, **hints):
        if model._meta.model_name == 'dry':
            return 'dry_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.model_name == 'dry':
            return 'dry_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.model_name == 'dry' or obj2._meta.model_name == 'dry':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == 'dry':
            return db == 'dry_db'
        return None
    
class PackagingRouter:
    route_app_labels = {'inventoryapp'}

    def db_for_read(self, model, **hints):
        if model._meta.model_name == 'packaging':
            return 'packaging_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.model_name == 'packaging':
            return 'packaging_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.model_name == 'packaging' or obj2._meta.model_name == 'packaging':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == 'packaging':
            return db == 'packaging_db'
        return None