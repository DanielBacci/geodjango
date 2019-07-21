def before_all(context):
    context.USE_PDB = context.config.userdata.getbool('PDB')
    env = context.config.userdata.get('ENV', 'dev')

    context.access_token = 'jovem'
    context.change_price_permission_access_token = 'jovem_change_price'

    defaults = {
        'dev': {
            'base_url': 'http://localhost:8000'
        }
    }
    context.settings = defaults[env]


def after_step(context, step):
    if context.USE_PDB and step.status == 'failed':
        import pdb
        pdb.post_mortem(step.exc_traceback)
