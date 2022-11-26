
# função para acessar os users
def get_users(user):
    if user == None: return

    from Models.Role import get_role
    from Models.User import get_users_of_team, get_users_of_group
    from Models.Rating import get_ratings_from_user, get_ratings
    from Models.Sprint import current_rating_period
    from Time import today

    sprint = current_rating_period(user.group_id)
    if sprint is None: return [[], []]

    #pego o nome e funções da pessoa que logou
    role = get_role(user.role_id)    

    #lista com as linhas da tabela ratings que correspondem a avaliações do usuário logado
    ratings = get_ratings(
        from_user_id=user.id, 
        sprint_id=sprint.id
    )

    for rating in ratings:
        print(rating)

    # ratings = get_ratings_from_user(user.id)
    grade_submitted = []
    grade_to_submit = []
    
    if user.role_id in [3, 4, 5]:
        # retorna lista com todos os usuários que são do mesmo time que o logado
        rate_users = get_users_of_team(user.team_id)
        
        for member in rate_users:
            if ratings is None or len(ratings) < 1:
                grade_to_submit.append(member)
                continue
            for rating in ratings:
                if member.id == rating.to_user_id:
                    grade_submitted.append(member)
                    break
            else:
                grade_to_submit.append(member)
        return [grade_to_submit, grade_submitted]

    rate_users = get_users_of_group(user.group_id)
    for group_member in rate_users:
        if group_member.role_id not in role.permissions_rate or group_member.team_id == '': continue
        if ratings is None or len(ratings) < 1:
            grade_to_submit.append(group_member)
            continue
        for rating in ratings:
            if group_member.id == rating.to_user_id and rating.value != '':
                grade_submitted.append(group_member)
                break
        else:
            grade_to_submit.append(group_member)
    return [grade_to_submit, grade_submitted]


def get_feedbacks (user_id, sprint_id):
    from random import randint
    return [
        [randint(0, 4) ,'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse quis suscipit lectus. Cras convallis enim tempor tellus ornare, sit amet.']
        for _ in range(10)
    ]


















