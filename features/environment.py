def before_all(context):
    context.USE_PDB = context.config.userdata.getbool('PDB')
    env = context.config.userdata.get('ENV', 'dev')

    defaults = {
        'dev': {
            'base_url': 'http://localhost:8000',
            'client_id': 'A91c1S8yRcMeE3iDYo22EnOcaxzsXTKGzHA78e7A',
            'client_secret': 'SBOLrrG0YpSuwCpWq8iRKvNEwUEDYyIRDE1pdCItgUZftC4V9IqMLxQIEB9salpp1mi9YMfnayhPGq59dNhS5T3eGaZVrZVGVYysaUnwTVOtVwNnvqJ57EusReJRbkro', # NOQA
        },
    }

    context.settings = defaults[env]


def after_step(context, step):
    if context.USE_PDB and step.status == 'failed':
        import pdb
        pdb.post_mortem(step.exc_traceback)
