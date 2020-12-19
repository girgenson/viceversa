from django.shortcuts import render

def main(request):
    return render(request, 'main_temp.html', {'greeting': 'Welcome'})


def to_reverse(request):
    request_get_free_input = request.GET['free_input'].strip()
    input_list = request_get_free_input.split(' ')
    len_list = len(input_list)
    reversed_text = request_get_free_input[::-1]
    return render(request, 'reverse_temp.html', {'free_input': request_get_free_input,
                                                 'reversed_input': reversed_text,
                                                 'list_len': len_list,
                                                 'input_list': input_list})

