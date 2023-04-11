# preamble_collection_tool

Tool to scan through a given source code base and detect, process, analyze, and catalog, all source code name identifiers, then determine if the those identifier names contain preambles.

This tool is the implmentation of the Graduate Capstone Project: _Automated Detection and Analysis of Common Preambles and Their Meanings in Source Code Identifiers_

### Capstone Project Abstract

> The interpretation of identifier names is a significant problem in software development. Programmers must interpret
identifier names before performing any software development or maintenance task, code search and analysis techniques
use identifier names to provide useful services to developers. Having high quality identifier names reduces the amount of
time developers spend reading code and the increases the accuracy of techniques that use natural language information
to support developers. Preambles are a particular type of token found in identifiers. Unlike typical tokens, Preambles add
no new information to the meaning of am identifier’s name—but instead specify certain types of behavior (e.g., pointers)
or help namespace (e.g., in the case of the C programming language) identifiers to a specify module. Because preambles
add no new information, they should be removed from, or at least identified in, identifiers before code analysis tries to
interpret identifier name meaning. The goal of my project is to validate and augment the types of preambles described in
prior work and create a technique that can automatically detect preambles.

## Dependencies & Installation

Before using preamble_collection_tool, the following dependencies must be installed:

1. [srcML](https://github.com/srcML/srcML)
2. [srcml_identifier_getter_tool](https://github.com/SCANL/srcml_identifier_getter_tool)
3. [spiral](https://github.com/casics/spiral)
4. [PyEnchant](https://pyenchant.github.io/pyenchant/)

It is important to note that as of now, preamble_collection_tool, is not platform independent, and **will only run on Unix based operating systems (ie. Linux, or OSX)**

After properly installing all necessary dependencies, create 3 new directories/folders in the main working directory:

1. `projects/`
2. `reports/`
3. `analysis/`

After creating these directories, clone/download source code projects that you desire to analyze into the newly created `projects` directory.

**NOTE: This tool currently only detects identifiers from source code files written in C, C++, C#, and Java**

## Usage & Operation

The tool is run through the following command: `python3 preamble_tool.py [OPTION]` 

There are a number of commands to run for operation:

1. `preamble_tool.py --help` or `preamble_tool.py -h` - Displays the help/options menu for reference.

2. `preamble_tool.py --collect-project data` or `preamble_tool.py -cpd` - Collects the name identifiers from all source files in all `projects` directory. Collected raw data from projects will be put into the `reports` directory.

3. `preamble_tool.py --collect-first-terms` or `preamble_tool.py -cft` - Scans all files in the `reports` directory and collects the most commonly used first terms of identifiers in all projects. Outputs two CSV files into the `analysis` directory. One of these files, `dictionary_first_terms.csv` contains first terms that are in the English dictionary, while `other_first_terms.csv` contains all others. These files contain all individual first terms of identifiers used in all analyzed projects, as well as how often these first terms are used in all instances, as well as an example identifier, and location of said example.

4. `preamble_tool.py --analyze-project-data` or `preamble_tool.py -apd` - Analyzes all gathered data in the `reports` directory, and runs full analysis to determine which identifiers in all projects contain preambles. Outputs final analysis results into `preamble_identifiers.csv`, located in the `analysis` directory.

## Research References & Sources

The heuristics and scientific basis from which this tool collects, gathers, and analyzes source code name identifiers is based on research conducted by various scientific sources.

These sources are:

1. [Source Code Analysis and Natural Language Laboratory](https://github.com/SCANL)
2. [Identifier Naming Structure Catalogue](https://github.com/SCANL/identifier_name_structure_catalogue)
3. [SCANL Datasets](https://github.com/SCANL/datasets)
4. [Socio-Technical Grounded Theory for Software Engineering](https://arxiv.org/pdf/2103.14235.pdf)
5. [On the Generation, Structure, and Semantics of Grammar Patterns in Source Code Identifiers](https://arxiv.org/pdf/2007.08033.pdf)