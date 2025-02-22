# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------


class TestStandardPythonParameterType(object):

    def test_standard_handling(self, decorated_standard_func):
        standard_input = {'name': ['Sarah'], 'state': ['WA']}
        state = {'state': ['WA']}
        result = decorated_standard_func(standard_input)
        assert state == result

        standard_input = {'param': {'name': ['Sarah'], 'state': ['WA']}}
        result = decorated_standard_func(**standard_input)
        assert state == result
