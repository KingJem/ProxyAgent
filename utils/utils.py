import random

import settings


def to_json(all_vendors):
    v = [ven.to_dict() for ven in all_vendors]
    return v


def random_target_web():
    target_web = random.choice(settings.RANDOM_TARGET_WEB)
    return target_web
