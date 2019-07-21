from behave import step


@step(u'I see "{status_code:d}" as response status code')
def verify_status_code(context, status_code):
    assert context.response.status_code == status_code, (
        'Expected status code {expected}, '
        'but response status code is {found}, '
        'and response content is {content}'.format(
            expected=status_code,
            found=context.response.status_code,
            content=context.response.content
        )
    )
