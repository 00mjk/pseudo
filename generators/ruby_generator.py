from pseudon.code_generator import CodeGenerator


class RubyGenerator(CodeGenerator):

    templates = {
        'program': '%code~join<\n>~'
        'function': 'def %name(%args~join<,>):\n' +
                    '%body~indent<1>~' +
                    'end\n'
    }