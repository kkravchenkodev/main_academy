def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(*args, **kwargs):
            return f"<{tag_name}>{func(*args, **kwargs)}</{tag_name}>"
        return func_wrapper
    return tags_decorator


@tags("div")
@tags("p")
@tags("span")
@tags("li")
def get_text(first, second, third):
    return f" Hello  -  {first} {second} {third}"


print(get_text("NAME", "SURNAME", "KJKSAHD"))
