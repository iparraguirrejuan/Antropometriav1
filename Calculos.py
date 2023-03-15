import math

#area muscular del brazo 
def camb(brazo_relajado,tricipital,sexo):
    area_muscular_brazo = 0
    if sexo == "f":
        area_muscular_brazo = round(float(((brazo_relajado-(0.31416*tricipital))**2/(4*math.pi)-6.5)),2)
    if sexo == "m":
        area_muscular_brazo = round(float(((brazo_relajado-(0.31416*tricipital))**2/(4*math.pi)-10)),2)
    return area_muscular_brazo


def masa_muscular_total(altura,camb):
    mmt = 0
    mmt = altura*(0.0264+(0.0029*camb))
    mmt = round(float(mmt),2)
    return mmt


def dencidad_corporal(sexo,edad,tricipital,subescapular,suprailiaco,bicipital):
    
    dc = 0
    sumatoria = float(tricipital + subescapular + suprailiaco + bicipital)
    if sexo == "m":
        if edad >= 17 and edad <= 19:
            dc = 1.1620 - (0.0630*(math.log(sumatoria)))   
        if edad >= 20 and edad <= 29:
            dc = 1.1631 - (0.00632*(math.log(sumatoria)))
        if edad >= 30 and edad <= 39:
            dc = 1.1422 - (0.0544*(math.log(sumatoria)))
        if edad >= 40 and edad <= 49:
            dc = 1.1620 - (0.0700*(math.log(sumatoria)))
        if edad >= 50:
            dc = 1.1715 - (0.0779*(math.log(sumatoria)))       
        return dc
    if sexo == "f":
        if edad >= 17 and edad <= 19:
            dc = 1.1549 - (0.0678*(math.log(sumatoria)))   
        if edad >= 20 and edad <= 29:
            dc = 1.1599 - (0.0717*(math.log(sumatoria)))
        if edad >= 30 and edad <= 39:
            dc = 1.1423 - (0.0632*(math.log(sumatoria)))
        if edad >= 40 and edad <= 49:
            dc = 1.1333 - (0.0612*(math.log(sumatoria)))
        if edad >= 50:
            dc = 1.1339 - (0.0645*(math.log(sumatoria)))
        return dc
    dc = round(float(dc),2)
    return sexo 



def masa_grasa(tipo_ecuacion, dc, peso):
    grasa_siri_kg = 0
    grasa_brosek_kg = 0
    if tipo_ecuacion == 1:
        grasa_siri = round(float((495/dc)-450),2)
        grasa_siri_kg = round(float((grasa_siri*peso)/100),2)
        return grasa_siri_kg
    if tipo_ecuacion == 2:
        grasa_brosek = round(float((457/dc)- 414),2)
        grasa_brosek_kg = round(float((grasa_brosek*peso)/100),2)
        return grasa_brosek_kg
    return tipo_ecuacion


def masa_osea(altura,diametro_wrist,diametro_femur):
    masa_o = 0
    altura_m = float(altura/100)
    wrist_m = float(diametro_wrist/100)
    femur_m = float(diametro_femur/100)
    masa_o =round(float(3.02*((altura_m)**2*wrist_m*femur_m*400)**0.712),2) 
    return masa_o 


def masa_residual(peso,masa_muscular_t,masa_grasa,masa_osea):
    masa_r = 0
    masa_r = round(float(peso - (masa_muscular_t + masa_grasa + masa_osea)),2)
    return masa_r


def masa_libre_grasa(peso,masa_grasa):
    masa_libre_g = 0
    masa_libre_g = round(float(peso - masa_grasa),2)
    return masa_libre_g


def indice_masa_corporal(peso,altura):
    imc = 0
    altura_m = altura/100
    imc =round(float(peso/(altura_m**2)),2)
    return imc


def indice_cintura_cadera(c_cintura, c_cadera):
    icc = 0
    icc = round(float(c_cintura/c_cadera),2)
    return icc


def peso_ideal_max(altura):
    peso_i_max = 0
    altura_m = altura/100
    peso_i_max = round(float(24.9 * (altura_m)**2),2)
    return peso_i_max

def peso_ideal_min(altura):
    peso_i_min = 0
    altura_m = altura/100
    peso_i_min = round(float(18.5 * (altura_m)**2),2)
    return peso_i_min
     

def endomorfia(tricipital,subescapular,supraespinal,altura):
    endo = 0
    x = float(tricipital + subescapular + supraespinal)
    x_corregido = x *170.18/altura
    endo = 0.7182 + (0.1451*x_corregido) - 0.00068*(x_corregido)**2 + 0.0000014*(x_corregido)**3
    endo = round(float(endo),2)
    return endo

def mesomorfia(humero,femur,tricipital,brazo_contraido,c_pantorilla,pi_pantorrilla,altura):
    meso = 0
    brazo_corregido = brazo_contraido - (tricipital/10)
    pierna_corregida = c_pantorilla - (pi_pantorrilla/10)
    meso = 0.858*humero + 0.601*femur + 0.188*brazo_corregido + 0.161*pierna_corregida - 0.131*altura + 4.5
    meso = round(float(meso),2)
    return meso


def ectomorfia (peso,altura):
    ectomor = 0
    indice_ponderal = round(float(altura/(peso**(1/3))),2)

    if indice_ponderal <= 38.28:
        ectomor = 0.1
    if indice_ponderal > 38.28 and indice_ponderal < 40.75:
        ectomor = (indice_ponderal*0.463) - 17.63
    else:
        ectomor = (indice_ponderal*0.732) - 28.58 
    ectomor = round(float(ectomor),2)
    return ectomor
    
def grafico (ectomorfia,endomorfia,mesomorfia):
    x =  round(float(ectomorfia - endomorfia),2)
    y = round(float((2*mesomorfia - (ectomorfia + endomorfia))),2)


