import database_facade as dbf
import sys
sys.path.append('./src')
sys.path.append('./src/models')

from skill import Skill
from helper import valida_autenticacao

@valida_autenticacao
def get_skill_by_id(id: int, *args, **kargs) -> Skill:
    """
    Get a skill by id
    Args:
        id(int): skill id
    Returns:
        Skill: skill object
    """
    skill = dbf.select('skill', ['skill_id', 'skill_name'], {'skill_id': id})[0]
    if skill:
        return Skill(skill[1], skill[0])
    return None

@valida_autenticacao
def get_skills(*args, **kargs) -> list:
    """
    Get all skills
    Returns:
        list: list of skills
    """
    skills = dbf.select('skill', ['skill_id', 'skill_name'])
    return [Skill(skill[1], skill[0]) for skill in skills] if skills else None

@valida_autenticacao
def create_skill(skill: Skill, *args, **kargs) -> Skill:
    """
    Create a new skill
    Args:
        skill(Skill): skill object
    Returns:
        Skill: skill created
    """
    data = {
        'skill_name': skill.name
    }
    id = dbf.insert('skill', data, return_columns=('skill_id',))[0]
    skill._id = id
    return skill