# 根据键获取对应的值
class GetJsonValue:
    def get_json_value_by_key(self, in_json, target_key, results=None):
        if results is None:
            results = []
        if isinstance(in_json, dict):
            for key in in_json.keys():
                value_data = in_json[key]
                self.get_json_value_by_key(value_data, target_key, results=results)
                if key == target_key:
                    results.append(value_data)
        elif isinstance(in_json, list) or isinstance(in_json, tuple):
            for result_data in in_json:
                self.get_json_value_by_key(result_data, target_key, results=results)
        return results
