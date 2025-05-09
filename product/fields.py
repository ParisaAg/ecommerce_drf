


from django.core import checks
from django.core.exceptions import ObjectDoesNotExist
from django.db import models


from django.db import models
from django.core.exceptions import ValidationError


class OrderField(models.PositiveIntegerField):
    description = "Ordering field on a unique field"

    def __init__(self, unique_for_field=None, *args, **kwargs):
        self.unique_for_field = unique_for_field
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        """
        Sets the order value automatically if not provided.
        Ensures the related object is saved before using it.
        """
        value = getattr(model_instance, self.attname)

        if value is None:
            qs = self.model.objects.all()

            if self.unique_for_field:
                related_obj = getattr(model_instance, self.unique_for_field)

                # بررسی اینکه فیلد مرتبط ذخیره شده باشه
                if related_obj is None or not hasattr(related_obj, "pk") or related_obj.pk is None:
                    raise ValidationError(
                        f"Cannot set order automatically because `{self.unique_for_field}` is not saved yet."
                    )

                qs = qs.filter(**{self.unique_for_field: related_obj})

            last_item = qs.order_by("-" + self.attname).first()
            value = 1 if last_item is None else last_item.order + 1
            setattr(model_instance, self.attname, value)

        return super().pre_save(model_instance, add)


    def _check_for_field_attribute(self, **kwargs):
        if self.unique_for_field is None:
            return [
                checks.Error("OrderField must define a 'unique_for_field' attribute")
            ]
        elif self.unique_for_field not in [
            f.name for f in self.model._meta.get_fields()
        ]:
            return [
                checks.Error(
                    "OrderField entered does not match an existing model field"
                )
            ]
        return []

    def pre_save(self, model_instance, add):

        if getattr(model_instance, self.attname) is None:
            qs = self.model.objects.all()
            try:
                query = {
                    self.unique_for_field: getattr(
                        model_instance, self.unique_for_field
                    )
                }
                qs = qs.filter(**query)
                last_item = qs.latest(self.attname)
                value = last_item.order + 1
            except ObjectDoesNotExist:
                value = 1
            return value
        else:
            return super().pre_save(model_instance, add)
