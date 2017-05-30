# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestSchema::test_food 1'] = {
    'data': {
        'foods': [
            {
                'name': 'A'
            },
            {
                'name': 'B'
            }
        ]
    }
}
