from marshmallow import fields

from prefect.utilities.serialization import JSONCompatible, OneOfSchema, ObjectSchema
from prefect.run_configs import KubernetesRun, LocalRun


class RunConfigSchemaBase(ObjectSchema):
    labels = fields.List(fields.String())


class KubernetesRunSchema(RunConfigSchemaBase):
    class Meta:
        object_class = KubernetesRun

    job_template_path = fields.String(allow_none=True)
    job_template = JSONCompatible(allow_none=True)
    image = fields.String(allow_none=True)
    env = fields.Dict(keys=fields.String(), allow_none=True)
    cpu_limit = fields.String(allow_none=True)
    cpu_request = fields.String(allow_none=True)
    memory_limit = fields.String(allow_none=True)
    memory_request = fields.String(allow_none=True)


class LocalRunSchema(RunConfigSchemaBase):
    class Meta:
        object_class = LocalRun

    env = fields.Dict(keys=fields.String(), allow_none=True)
    working_dir = fields.String(allow_none=True)


class RunConfigSchema(OneOfSchema):
    type_schemas = {
        "KubernetesRun": KubernetesRunSchema,
        "LocalRun": LocalRunSchema,
    }