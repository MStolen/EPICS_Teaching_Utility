\LoadClass[12pt]{article}
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{epics_docs}[2022/09/27 A custom class for EPICS Student Lists]

\RequirePackage[T1]{fontenc}

\RequirePackage[margin=1in]{geometry} %set margins
%\RequirePackage{indentfirst} %indent first paragraph in section

\RequirePackage[parfill]{parskip}

\RequirePackage{float}

%set header
\RequirePackage{fancyhdr}
    \setlength{\headheight}{14.5pt} %avoid header warning
    \renewcommand{\headrulewidth}{0pt}
    \pagestyle{fancy}
    \fancyhf{}
    \rhead{\@title}
    \lhead{EPICS}
    \fancyfoot{}
    \rfoot{\thepage}


%for custom colors
\RequirePackage[pdftex,dvipsnames]{xcolor}
    \definecolor{sectionColor}{RGB}{54,95,145}
    \definecolor{titleColor}{RGB}{23,54,93}

\RequirePackage{titlesec} %for modifying section spacing
    \titlespacing{\section}
    {0pt plus 2pt minus 4pt}{\the\baselineskip plus 2pt minus 4pt}{1\baselineskip}
    % \titleformat{\section}{\Large\raggedright\bf\color{sectionColor}}{\thesection~-~}{0em}{}[{\titlerule[0.8pt]}]
    \titleformat{\section}{\Large\raggedright\bf\color{sectionColor}}{}{0em}{}[{\titlerule[0.8pt]}]
    \titlespacing{\subsection}
    {0pt plus 2pt minus 4pt}{\the\baselineskip plus 2pt minus 4pt}{0\baselineskip}
%     \titleformat{\subsection}{\large\raggedright\bf\color{sectionColor}}{}{0em}{\thesubsection~-~}
%     \titleformat{\subsubsection}{\normalsize\raggedright\bf\color{sectionColor}}{\thesubsubsection~-~}{0em}{}
    \titleformat{\subsection}{\large\raggedright\bf\color{sectionColor}}{}{0em}{\thesubsection}
    \titleformat{\subsubsection}{\normalsize\raggedright\bf\color{sectionColor}}{\thesubsubsection}{0em}{}

\RequirePackage{xargs} % Use more than one optional parameter in a new commands
%\RequirePackage[pdftex,dvipsnames]{xcolor}  % Coloured text etc.

%used for creating notes in margins or inline
\setlength{\marginparwidth}{2.15cm}
\RequirePackage[colorinlistoftodos,prependcaption,textsize=tiny]{todonotes}
    \newcommandx{\unsure}[2][1=]{\todo[linecolor=red,backgroundcolor=red!25,bordercolor=red,#1]{#2}}
    \newcommandx{\change}[2][1=]{\todo[linecolor=blue,backgroundcolor=blue!25,bordercolor=blue,#1]{#2}}
    \newcommandx{\info}[2][1=]{\todo[linecolor=OliveGreen,backgroundcolor=OliveGreen!25,bordercolor=OliveGreen,#1]{#2}}
    \newcommandx{\improvement}[2][1=]{\todo[linecolor=Plum,backgroundcolor=Plum!25,bordercolor=Plum,#1]{#2}}
    \newcommandx{\thiswillnotshow}[2][1=]{\todo[disable,#1]{#2}}

% suppress warnings from todonotes being close together
\RequirePackage{silence}
    \WarningFilter*{latex}{Marginpar on page}

%package for figures
\RequirePackage{graphicx}
    \graphicspath{ {./Figures/} }
\RequirePackage{float}

%used so figures and tables are preceded by section num
\RequirePackage{chngcntr}
    \counterwithin{figure}{section}
    \counterwithin{table}{section}

%subfigures
\RequirePackage{subcaption}

\setlength{\parindent}{0pt}


% Remove section number
\makeatletter
\let\latexl@section\l@section
\def\l@section#1#2{\begingroup\let\numberline\@gobble\latexl@section{#1}{#2}\endgroup}
\makeatother

% Remove subsection and subsubsection numbers
\renewcommand{\thesubsection}{}
\renewcommand{\thesubsubsection}{}

% Universal notes lines for students
\RequirePackage{pgffor, ifthen}
\newcommand{\notes}[3][\empty]{%
    % \noindent Notes\vspace{40pt}\\
    \foreach \n in {1,...,#2}{%
        \ifthenelse{\equal{#1}{\empty}}
            {\rule{#3}{0.5pt}\\}
            {\rule{#3}{0.5pt}\vspace{#1}\\}
        }
}

% Prevent hyphenation of names
\hyphenpenalty=10000
\hbadness=10000

%Declare options here
%Passes all options that have not been handled to article class
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax %execute options

%new and renewed commands
%custom title
\renewcommand{\maketitle}{
    \begin{center}\huge{\textbf{\color{titleColor}\@title}}\end{center}
}
