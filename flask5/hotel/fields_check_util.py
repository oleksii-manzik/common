def check_if_all_parameters_is_filled(args):
    if not all(args.values()):
        return {'http_status_code': 400,
                'message': f'You haven\'t pass these parameters: '
                           f'{[x for x in args.keys() if not args[x]]}'}


def check_if_key_in_args(key, args, item_type):
    if not args[key]:
        return {'http_status_code': 400,
                'message': f'Please provide {key} of the {item_type}'}


def check_if_row_was_affected(result, item_type, identificator):
    if not result:
        return {'http_status_code': 404,
                'message': f'{item_type} {identificator} doesn\'t exist'}
