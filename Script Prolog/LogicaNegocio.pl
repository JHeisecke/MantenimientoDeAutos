

%%% =======================================================================
%%% Hechos de las personas. En todos los casos Y es la C.I. (Identificador)
%%% =======================================================================

cliente('100').
cliente('4222111').
asesor('5784596').
asesor('1').


% Hecho: es_nombre_de(X, Y) X es el nombre de Y es la C.I.
es_nombre_de('Pedro', '4222111').
es_nombre_de('Lucia', '5784596').

% Hecho: es_apellido_de(X, Y) X es el apellido de Y
es_apellido_de('Gonzales', '4222111').
es_apellido_de('Gomez', '5784596').

% Hecho: es_direccion_de(X, Y) X es el direccion de Y
es_direccion_de('San Lorenzo...', '4222111').
es_direccion_de('Asuncion...', '5784596').

% Hecho: es_telefono_de(X, Y) X es el telefono de Y
es_telefono_de('098457215', '4222111').
es_telefono_de('098345849', '5784596').

% Hecho: es_email_de(X, Y) X es el email de Y
es_email_de('pedro@gmail.com', '4222111').
es_email_de('lucia@gmail.com', '5784596').

%%%% Hechos de los clientes. En todos los casos Y es el C.I. (Identificador)

% Hecho: es_ruc_de(X, Y) X es el Ruc de Y
es_ruc_de('915512-1', '4222111').

%%%% Hechos de los asesores. En todos los casos Y es el C.I. (Identificador)

% Hecho: es_sueldo_de(X, Y) X es sueldo de Y
es_sueldo_de('1900000', '5784596').


%%% ==========================================================================
%%% Hechos de los repuestos. En todos los casos Y es el Codigo (Identificador)
%%% Las solicitudes se componen de repuestos que se crean en la propia solicitud
%%% ==========================================================================

repuesto('0001').

% Hecho: es_tipo_de_repuesto(X, Y) X es el tipo de Y
es_tipo_de_repuesto('Faro', '0001').

% Hecho: es_marca_de_repuesto(X, Y) X es la marca de Y
es_marca_de_repuesto('Rogers', '0001').

% Hecho: es_costo_de_repuesto(X, Y) X es el costo de Y
es_costo_de_repuesto('500000', '0001').

%%% ==========================================================================
%%% Hechos de los vehiculos. En todos los casos Y es la chapa (Identificadora)
%%% Las solicitudes se componen de vehiculos que se crean en la propia solicitud
%%% ==========================================================================
	
vehiculo('ABC-321').

% Hecho: es_marca_de_vehiculo(X, Y) X es el marca de Y
es_marca_de_vehiculo('Toyota', 'ABC-321').

% Hecho: es_modelo_de_vehiculo(X, Y) X es el modelo de Y
es_modelo_de_vehiculo('Corola', 'ABC-321').


%%% ==========================================================================
%%% Hechos de las solicitudes. En todos los casos Y es el Codigo (Identificador)
%%% ==========================================================================

solicitud('1').

% Hecho: es_fecha_de_solicitud(X, Y) X es la fecha de Y
es_fecha_de_solicitud('22/11/15', '1').

% Hecho: es_cliente_de_solicitud(X, Y) X es la cliente de Y
es_cliente_de_solicitud('4222111', '1').

% Hecho: es_asesor_de_solicitud(X, Y) X es la asesor de Y
es_asesor_de_solicitud('4123123', '1').

% Hecho: es_vehiculo_de_solicitud(X, Y) X es la vehiculo de Y
es_vehiculo_de_solicitud('321', '1').

%%% ----------------------------------------------------------------------------
%%% Los vehiculos se pueden agregar a las solicitudes

% Hecho: es_vehiculo_de_solicitud(X, Y) X es vehiculo de la solicitud de Y
es_repuesto_de_vehiculo('ABC-321', '1').

%%% ----------------------------------------------------------------------------
%%% Los repuestos se pueden agregar a las solicitudes

% Hecho: es_repuesto_de_solicitud(X, Y) X es repuesto de la solicitud de Y
es_repuesto_de_solicitud('0001', '1').


%%% ==========================================================================
%%% ===============================REGLAS=====================================
%%% ==========================================================================

%%% ----------------------------------------------------------------------------
%%% Regla: Son atributos del cliente con Cedula si
%%% nombre, apellido, direccion, telefono, email y ruc pertenecen a la Cedula
%%% y si Cedula es cliente

	son_datos_de_cliente(Cedula, Nombre, Apellido, Direccion, Tel, Mail, Ruc) :-
	cliente(Cedula),
	es_nombre_de(Nombre, Cedula), es_apellido_de(Apellido, Cedula),
	es_direccion_de(Direccion, Cedula), es_telefono_de(Tel, Cedula), 
	es_email_de(Mail, Cedula), es_ruc_de(Ruc, Cedula).


%%% ----------------------------------------------------------------------------
%%% Regla: Son atributos del asesor con Cedula si:
%%% nombre, apellido, direccion, telefono, celular, email y sueldo pertenecen a la Cedula
%%% y si Cedula es asesor

	son_datos_de_asesor(Cedula, Nombre, Apellido, Direccion, Tel, Mail, Sueldo) :-
	asesor(Cedula),
	es_nombre_de(Nombre, Cedula), es_apellido_de(Apellido, Cedula),
	es_direccion_de(Direccion, Cedula), es_telefono_de(Tel, Cedula), 
	es_email_de(Mail, Cedula), es_sueldo_de(Sueldo, Cedula).

	
%%% ----------------------------------------------------------------------------
%%% Regla: Son atributos del repuesto con Codigo si:
%%% tipo, marca, y costo pertenecen al Codigo

	son_datos_de_repuesto(Codigo, Tipo, Marca, Costo) :-
	es_tipo_de_repuesto(Tipo, Codigo), es_marca_de_repuesto(Marca, Codigo),
	es_costo_de_repuesto(Costo, Codigo).
	
	son_datos_de_repuesto(Codigo, Tipo, Marca, Costo) :-
	es_tipo_de_repuesto(Tipo, Codigo), es_marca_de_repuesto(Marca, Codigo),
	es_costo_de_repuesto(Costo, Codigo).

%%% ----------------------------------------------------------------------------
%%% Regla: Son atributos del vehiculo con Chapa si:
%%% marca y modelo pertenecen a la chapa

	son_datos_de_vehiculo(Chapa, Marca, Modelo) :-
	es_marca_de_vehiculo(Marca, Chapa), es_modelo_de_vehiculo(Modelo, Chapa).

%%% ----------------------------------------------------------------------------
%%% ----------------------------------------------------------------------------
%%% Regla: Son atributos de la solicitud con Codigo si:
%%% fecha, cliente, asesor, vehiculo y repuesto pertencen a la solicitud

	son_datos_de_solicitud(Codigo, Fecha, Cliente, Asesor, Vehiculo, Repuesto) :-
	es_fecha_de_solicitud(Fecha, Codigo), 
	es_cliente_de_solicitud(Cliente, Codigo), 
	es_asesor_de_solicitud(Asesor, Codigo), 
	es_repuesto_de_solicitud(Repuesto, Codigo), 
	es_vehiculo_de_solicitud(Vehiculo, Codigo).
	
	
% Javier Heisecke