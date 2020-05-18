from flask import Flask, render_template, url_for

app = Flask(__name__)

person = {
    'information':
    {
        'first_name': 'Guole',
        'last_name': 'YANG',
        'identity': 'Apprenant en Data Scientifique',
        'mail': 'yangguole@outlook.com',
        'birthday': '18 Avril, 1988',
        # 'adress': '1 Rue Alain Raillard',
        'city': 'Aubervilliers',
        'phone': '06 49 76 72 98',
        'resumes':
            [
                {
                    'p': "Passionné par l'informatique, j'ai étudié dans ce domaine où j'ai acquis la connaissance en programmation orientée objet, les langages de programmation (exemple de langage), le développement web et d'application mobile. De nature polyvalente et curieux, j'ai également exercé dans le commerce traditionnel et en ligne, ainsi qu'en restauration. "
                },
                {
                    'p': "En parallèle, j'ai fais un formation en Marketing et communication à un niveau Bachelor+3 dans une école de commerce en ligne (Comnicia). Toute ces expériences m'ont permit d'avoir une vision globale sur le fonctionnement d'une entreprise et en créer une. Et notamment des compétences que j’ai acquis: la relation clients,  la polyvalence et la gestion de stress. "
                },
                {
                    'p': "Pour pouvoir intégrer l’intelligence artificielle dans des sites d’internet et applications mobile et vers une domaine en plein développement,  je me suis inscrit à la formation data et intelligence artificielle à École IA Microsoft by Simplon ."
                }
            ]
    },
    'educations':
    [
        {'year': '2020',
            'school': 'Ecole IA Microsoft by Simplon',
            'formation': 'Data scientifique en IA'
         },

        {'year': '2020',
            'school': 'Apple Foundation Program by Simplon',
            'formation': 'Création d\'application mobile IOS'
         },

        {'year': '2018',
            'school': 'Google Atelier Numérique',
            'formation': 'Marketing digital'
         },

        {'year': '2017',
            'school': 'Ecole de commerce en ligne Comnicia',
            'formation': 'Marketing et communication',
         },
        {
            'year': '2008 - 2010',
            'school': 'Paris VII Didérot',
            'formation': 'Licence Informatique 1 et 2ième année'
        },
        {
            'year': '2008',
            'school': 'Lycée générale Turgot',
            'formation': 'Baccalauréat scientifique'
        }

    ],

    'experiences': [
        {},
        {},
        {}
    ],
    'skills':
        {
        'technique':
            [
                {
                    'skill': 'Python/R/Flask'
                },

                {
                    'skill': 'HTML/PHP/Javascript/Symfony'
                },
                {
                    'skill': 'GitHub/Docker'
                },
                {
                    'skill': 'MySQL'
                },
                {
                    'skill': 'Bootstrap'
                },
                {
                    'skill': 'Wordpress'
                },
                {
                    'skill': 'Swift'
                },
                {
                    'skill': 'SwiftUI'
                },
                {
                    'skill': 'Photoshop'
                }
            ],
        'professionel':
            [
                {
                    'skill': 'Travail en équipe',
                },
                {
                    'skill': 'Résolution de problème',
                },
                {
                    'skill': 'Marketing et communication',
                }
            ]
    },
    'interests':
        [
        {
            'interet': 'Lecture',
        },
        {
            'interet2': 'Jeux vidéo'
        },
        {
            'interet3': 'Photographie'
        }
    ],
    'languages':
        [
        {
            'langue': 'Chinois',
        },
        {
            'langue': 'Français'
        },
        {
            'langue': 'Anglais'
        }
    ],

    'liens':
        {
            'github': 'github.com/yanggautier',
            'linkedin': 'linkedin.com/in/guole-yang-409251167/',
            'instagram': 'www.instagram.com/guole/'
    }
}


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', person=person)


if __name__ == '__main__':
    app.run(debug=True)
