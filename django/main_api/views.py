from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.http import Http404, HttpResponse
from rest_framework import status

def request_validator(request,check_list):
	try:
		data=request.data
		for field in check_list:
			if field[1] is True and field[0] not in data:
				return [False, 'parameter (' + field[0] + ') is mising']
			elif field[1] is False and field[0] not in data:
				pass
			elif field[2] == 'any':
				pass
			elif isinstance(data[field[0]],eval(field[2])) is False:
				return [False, 'incorrect parameter type: field' + ' ' + str(field[0]) + ' is expected to be type ' + str(field[2]) + '. (' + str(data[field[0]]) + ') is not sufficient']
			else:
				pass
	except Exception as e:
		return False, ['Something Went Wrong']
	return True, None

def check_list(component_type):
    if component_type == 'resistor':
        check_list = [
                        ["description", False, 'any'],
                        ["tolerance", True, 'int'],
                        ["stability", True, 'int'],
                        ["reliability", True, 'int'],
                        ["voltage_coefficient", True, 'int'],
                        ["noise", True, 'int'],
                        ["temperature_rating", True, 'int'],
                        ["thermal_resistance", True, 'int'],
                        ["temperature_coefficient_of_resistance", True, 'int'],
                    ]
        return check_list					
    elif component_type == 'capacitor':
        check_list = [
                        ["description", False, 'any'],
                        ["nominal_capacitance", True, 'int'],
                        ["working_voltage", True, 'int'],
                        ["tolerance", True, 'int'],
                        ["working_temperature", True, 'int'],
                        ["temperature_coefficient", True, 'int'],
                    ]
        return check_list
    elif component_type == 'transistor':
        check_list = [
                        ["description", False, 'any'],
                        ["current_gain", True, 'int'],
                        ["collector_emitter_voltage", True, 'int'],
                        ["emitter_base_voltage", True, 'int'],
                        ["collector_current", True, 'int'],
                    ]
        return check_list

class BoardPost(APIView):

    def post(self, request):
        if not request.data:
            return Response('no data', status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                data = request.data["type"]
            except:
                return Response('type is a mandatory field', status=status.HTTP_400_BAD_REQUEST)

        check_list_res = check_list(request.data["type"])
        val_res = request_validator(request,check_list_res)
        if not val_res[0]:
            return Response(val_res[1], status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(request.data, status=status.HTTP_200_OK)
