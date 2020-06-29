def solution(skills, skill_trees):
    possible_skill_tree_count = 0

    for skill_tree in skill_trees:
        is_possible_skill_tree = True
        containing_skills = []

        for skill in skill_tree:
            if skill in skills:
                containing_skills.append(skill)

        for index, containing_skill in enumerate(containing_skills):
            if containing_skill != skills[index]:
                is_possible_skill_tree = False

        if is_possible_skill_tree:
            possible_skill_tree_count += 1

    return possible_skill_tree_count


print(solution('CBD', ["BACDE", "CBADF", "AECB", "BDA"]))