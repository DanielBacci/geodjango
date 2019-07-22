def before_all(context):
    context.USE_PDB = context.config.userdata.getbool('PDB')
    env = context.config.userdata.get('ENV', 'dev')

    defaults = {
        'dev': {
            'base_url': 'http://localhost:8000',
            'client_id': 'kYjoNWfjcFJE7Gcb74FekEGlP6fkXbHW4S2KWfIS',
            'client_secret': (
                'uhsLkltzfD58UlmobjqvgMKfwBA677sTRHQs6ZLuoRXiU0no'
                'OV3tEzgZm1xivrQrJpVvlJHzTYa3ZCYrs9Jy4WWCc7V2QeVcr'
                'TW1c2jepfc5TAbO0QHUNJtYRsxFpb2G'
            )
        }
    }
    context.settings = defaults[env]


def after_step(context, step):
    if context.USE_PDB and step.status == 'failed':
        import pdb
        pdb.post_mortem(step.exc_traceback)
