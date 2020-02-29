from chaos_lib import corrupt_delay


@corrupt_delay
def handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }
