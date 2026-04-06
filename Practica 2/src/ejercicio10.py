from collections import Counter 
def ranking ():
    rounds = [
        {
            'theme': 'Entrada',
            'scores': {
                'Valentina': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
                'Mateo': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
                'Camila': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
                'Santiago': {'judge_1': 6, 'judge_2': 7, 'judge_3': 6},
                'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 8},
            }
        },
        {
            'theme': 'Plato principal',
            'scores': {
                'Valentina': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
                'Mateo': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
                'Camila': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
                'Santiago': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
                'Lucía': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
            }
        },
        {
            'theme': 'Postre',
            'scores': {
                'Valentina': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
                'Mateo': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
                'Camila': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
                'Santiago': {'judge_1': 7, 'judge_2': 7, 'judge_3': 6},
                'Lucía': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
            }
        },
        {
            'theme': 'Cocina internacional',
            'scores': {
                'Valentina': {'judge_1': 8, 'judge_2': 9, 'judge_3': 9},
                'Mateo': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
                'Camila': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
                'Santiago': {'judge_1': 8, 'judge_2': 9, 'judge_3': 7},
                'Lucía': {'judge_1': 7, 'judge_2': 7, 'judge_3': 8},
            }
        },
        {
            'theme': 'Final libre',
            'scores': {
                'Valentina': {'judge_1': 9, 'judge_2': 8, 'judge_3': 9},
                'Mateo': {'judge_1': 8, 'judge_2': 9, 'judge_3': 8},
                'Camila': {'judge_1': 7, 'judge_2': 7, 'judge_3': 7},
                'Santiago': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
                'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 7},
            }
        }
    ]

    leaderboard = {}

    for i, round in enumerate(rounds):
        round_scores = {}
        for name, judges_info in round['scores'].items():
            score = sum(judges_info.values())

            if name in leaderboard:
                leaderboard[name]['total'] += score
                leaderboard[name]['scores'].append(score)
            else:
                leaderboard.update({
                    name: {
                    'total': score,
                    'scores': [score],
                    'wins': 0
                    }
                })

            round_scores[name] = score
        
      
        winner = max(round_scores, key = round_scores.get)
        leaderboard[winner]['wins'] += 1

        
        print(f'Ronda {i+1} - {round['theme']}')
        print(f' Ganador: {winner} ({round_scores[winner]} pts)')
        print()

        final_ranking = sorted(leaderboard.items(), key=lambda x: x[1]['total'], reverse=True)

        print('Tabla de posiciones: ') 
        for name, data in final_ranking:
            print(f'Cocinero: {name}')
            print(f'Puntaje: {data['total']}')
            print(f'Rondas Ganadas: {data['wins']}')
            print(f'Mejor Ronda: {max(data['scores'])}')
            print(f'Promedio: {sum(data['scores']) / len(data['scores']):.1f}')
            print()

