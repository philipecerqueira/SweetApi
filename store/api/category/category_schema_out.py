from ninja import Schema


class CategorySchemaOut(Schema):
    id: int
    title: str