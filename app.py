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
    'formations':
    [
        {'year': '2020 ',
            'school': 'Ecole IA Microsoft by Simplon',
            'identity': 'Data scientifique en IA'
         },

        {'year': '2020',
            'school': 'Apple Foundation Program by Simplon',
            'identity': 'Création d\'application mobile IOS'
         },

        {'year': '2019',
            'school': ' Openclassroom.com , W3cschool.com',
            'identity': 'Création de site web'
         },

        {'year': '2018',
            'school': 'Google Atelier Numérique',
            'identity': 'Marketing digital'
         },

        {'year': '2017',
            'school': 'Ecole de commerce en ligne Comnicia',
            'identity': 'Marketing et communication',
         },
        {
            'year': '2008 - 2010',
            'school': 'Paris VII Didérot',
            'identity': 'Licence Informatique 1 et 2ième année'
        },
        {
            'year': '2008',
            'school': 'Lycée générale Turgot',
            'identity': 'Baccalauréat scientifique'
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
                    'skill': 'Analyse des données'
                },
                {
                    'skill': 'Web scraping'
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
                    'skill': 'Swift/SwiftUI'
                },
                {
                    'skill': 'Photoshop'
                }
            ],
        'professionel':
            [
                {
                    'skill': 'Travail en équipe',
                }
            ]
    },
    'interests':
        [
            {
                'interet': 'Lecture',
            },

            {
                'interet': 'Jeux vidéo'
            },

            {
                'interet': 'Photographie'
            }
    ],
    'languages':
        [
        {
            'langue': 'Chinois',
            'level': 'Langue maternelle'
        },
        {
            'langue': 'Français',
            'level': 'Bilingue'
        },
        {
            'langue': 'Anglais',
            'level': 'Scolaire'
        }
    ],

    'liens':
        {
            'github': 'github.com/yanggautier',
            'linkedin': 'linkedin.com/in/guole-yang-409251167/',
            'instagram': 'www.instagram.com/guole/'
    },
    'projects':
        [
            {
                'name': "Application mobile IOS Youpigoo",
                'description':
                    [
                        {
                            'p': "Ce projet consite créer une application mobile IOS à partir d'une simple idée à la conception puis à la réalisation."
                        },
                        {
                            'p': "Cette application sert à organiser et optimiser le voyaege selon 3 critères: temps, l'argent et le rythme de voyage"
                        }
                    ],
                'status': 'En équipe'
            }
    ]
}


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', person=person)


if __name__ == '__main__':
    app.run(debug=True)
