from .nodes.form_submit_node import FormSubmitNode



NODE_CLASS_MAPPINGS = {
    "FormSubmitNode":FormSubmitNode,
}
NODE_DISPLAY_NAMES_MAPPINGS = {
    "FormSubmitNode": "FormSubmitNode"
}
WEB_DIRECTORY = "./js"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAMES_MAPPINGS','WEB_DIRECTORY']