-- Tabla donde se agregan los pacientes que son atendidos
CREATE TABLE [pacientes] (
    [paciente_id] int  NOT NULL ,
    [turno_id] int  NOT NULL ,
    [dx_id] int  NOT NULL ,
    [hora_ingreso] time  NOT NULL ,
    [hora_egreso] time  NOT NULL ,
    [laboratorios] boolean  NOT NULL ,
    [imagenes] boolean  NOT NULL ,
    [interconsulta] NOT NULL,
    [salida_id] int  NOT NULL ,
    [edad] int NOT NULL,
    [sexo] CHAR(1) NOT NULL,
    [triage] int NOT NULL,
    CONSTRAINT [PK_pacientes] PRIMARY KEY CLUSTERED (
        [paciente_id] ASC
    )
)
-- Tabla donde se agregan las caracteristicas de cda turno que hago
CREATE TABLE [turnos] (
    [turno_id] int  NOT NULL ,
    [nombre] varchar(30)  NOT NULL ,
    [hora_inicio] time  NOT NULL ,
    [hora_final] time  NOT NULL ,
    [fecha] date  NOT NULL ,
    [n_pacientes] int  NOT NULL ,
    CONSTRAINT [PK_turnos] PRIMARY KEY CLUSTERED (
        [turno_id] ASC
    )
)

-- Aqui se agregan los tipos de diagnosticos
CREATE TABLE [diagnosticos] (
    [dx_id] int  NOT NULL ,
    [tipo_dx] varchar(30)  NOT NULL ,
    CONSTRAINT [PK_diagnosticos] PRIMARY KEY CLUSTERED (
        [dx_id] ASC
    )
)

-- Aqui se agregan los tipos de salidas al finalizar la atencion
CREATE TABLE [salidas] (
    [salida_id] int  NOT NULL ,
    [tipo_salida] varchar(30)  NOT NULL ,
    CONSTRAINT [PK_salidas] PRIMARY KEY CLUSTERED (
        [salida_id] ASC
    )
)

-- FK para identiciar en que turno se atendio qué paciente
ALTER TABLE [pacientes] WITH CHECK ADD CONSTRAINT [FK_pacientes_turno_id] FOREIGN KEY([turno_id])
REFERENCES [turnos] ([turno_id])

ALTER TABLE [pacientes] CHECK CONSTRAINT [FK_pacientes_turno_id]

-- FK para identificar el tipo de diagnostico
ALTER TABLE [pacientes] WITH CHECK ADD CONSTRAINT [FK_pacientes_dx_id] FOREIGN KEY([dx_id])
REFERENCES [diagnosticos] ([dx_id])

ALTER TABLE [pacientes] CHECK CONSTRAINT [FK_pacientes_dx_id]

-- FK para identificar el tipo de salida
ALTER TABLE [pacientes] WITH CHECK ADD CONSTRAINT [FK_pacientes_salida_id] FOREIGN KEY([salida_id])
REFERENCES [salidas] ([salida_id])

ALTER TABLE [pacientes] CHECK CONSTRAINT [FK_pacientes_salida_id]