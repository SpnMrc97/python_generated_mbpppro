def deep_extract_singly(nested_list):
    def flatten(current_list):
        for item in current_list:
            if isinstance(item, list):
                yield from flatten(item)
            else:
                yield item

    return set(flatten(nested_list))
