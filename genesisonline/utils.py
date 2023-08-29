def get_api_params(func_args: dict, exclude: list = list()) -> dict:
    exclude.extend(["self", "__class__"])
    api_params = func_args.pop("kwargs", dict())
    for k, v in func_args.items():
        if k not in exclude:
            api_params[k] = v
    return api_params
