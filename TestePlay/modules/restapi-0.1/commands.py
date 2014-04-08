# Here you can create play commands that are specific to the module, and extend existing commands
# -*- coding: utf-8 -*-

MODULE = 'restapi'

# Commands that are specific to your module

COMMANDS = ['restapi:messagefile','restapi:sample']

def execute(**kargs):
    command = kargs.get("command")
    app = kargs.get("app")
    args = kargs.get("args")
    env = kargs.get("env")

    if command == "restapi:messagefile":
        print "~ Criando o arquivo conf/result_messages.properties..."
        try:
            f = open("conf/result_messages.properties", "w")
            try:
                f.write('# Default messages\n')
                f.write('# 0=Requisição Realizada com Sucesso\n')
                f.write('# 1=Exceção de Sistema\n')
                f.write('# 2=Exceção de Validação\n')
                f.write('\n')
                f.write('3=Registro não encontrado\n')
                f.write('4=Parametro não informado\n')
                
                print "~ Arquivo gerado com sucesso.\n"
                
            finally:
                f.close()
        except IOError:
            pass
        
            
    if command == "restapi:sample":
        print "~ Criando o arquivo models/Usuario.java..."
        try:
            f = open("app/models/Usuario.java", "w")
            try:
                f.write('package models;\n')
                f.write('\n')
                f.write('import javax.persistence.Entity;\n')
                f.write('import play.db.jpa.Model;\n')
                f.write('\n')
                f.write('@Entity\n')
                f.write('public class Usuario extends Model{\n')
                f.write('\n')
                f.write('    public String nome;\n')
                f.write('    public String email;\n')
                f.write('\n')
                f.write('    @Override\n')
                f.write('    public String toString(){\n')
                f.write('        return nome;\n')
                f.write('    }\n')
                f.write('\n')
                f.write('}\n')
                
            finally:
                f.close()
        except IOError:
            pass

        print "~ Criando o arquivo controllers/Usuarios.java..."
        try:
            f = open("app/controllers/Usuarios.java", "w")
            try:
                f.write('\n')
                f.write('package controllers;\n')
                f.write('\n')
                f.write('import api.wadl.annotation.Param;\n')
                f.write('import api.wadl.annotation.Path;\n')
                f.write('import api.wadl.annotation.Paths;\n')
                f.write('import api.wadl.annotation.Resource;\n')
                f.write('import java.util.List;\n')
                f.write('import models.Usuario;\n')
                f.write('import utils.Result;\n')
                f.write('import controllers.restapi.DefaultController;\n')
                f.write('\n')
                f.write('@Resource(name="usuarios",param={@Param(name="{id}",type="int")})\n')
                f.write('public class Usuarios extends DefaultController {    \n')
                f.write('    \n')
                f.write('    @Path(method="GET",id="getAllUsuario")\n')
                f.write('    public static void listAll(){\n')
                f.write('        List<Usuario> usuarios = Usuario.findAll();			\n')
                f.write('        renderObject(Result.OK(usuarios));\n')
                f.write('    }\n')
                f.write('    \n')
                f.write('    @Path(name="/{id}",method="GET",id="getUsuarioById")\n')
                f.write('    public static void findId(Long id) {\n')
                f.write('        if(id != null) {\n')
                f.write('            Usuario usuario = Usuario.findById(id);\n')
                f.write('            if(usuario!=null){\n')
                f.write('		        renderObject(Result.OK(usuario));\n')
                f.write('            }else{\n')
                f.write('                //Registro nao encontrado\n')
                f.write('		        renderObject(Result.ERROR(3));\n')
                f.write('            }\n')
                f.write('        }else{\n')
                f.write('            //Parametro nao informado\n')
                f.write('	        renderObject(Result.ERROR(4));\n')
                f.write('        }       \n')
                f.write('    }\n')
                f.write('    \n')
                f.write('    \n')
                f.write('    @Path(name="/{id}",method="DELETE",id="deleteUsuario")\n')
                f.write('    public static void delete(Long id) {\n')
                f.write('        try {\n')
                f.write('            Usuario usuario = Usuario.findById(id);\n')
                f.write('            if(usuario!=null){\n')
                f.write('                usuario.delete();\n')
                f.write('                renderObject(Result.OK("Usuario apagado com sucesso."));\n')
                f.write('            }else{\n')
                f.write('                //Registro nao encontrado\n')
                f.write('                renderObject(Result.ERROR(3));\n')
                f.write('            }\n')
                f.write('        } catch (Exception ex) {\n')
                f.write('            //Erro de sistema\n')
                f.write('            renderObject(Result.SYSERROR(ex.getMessage()));\n')
                f.write('        }\n')
                f.write('    }\n')
                f.write('    \n')
                f.write('    @Paths(\n')
                f.write('        {\n')
                f.write('            @Path(method="POST",id="addUsuario" ,param={\n')
                f.write('                @Param(name="usuario.nome",type="string"),\n')
                f.write('                @Param(name="usuario.email",type="string")\n')
                f.write('            }),\n')
                f.write('            @Path(name="/{id}",id="saveUsuario",method="PUT", param={\n')
                f.write('                @Param(name="usuario.nome",type="string"),\n')
                f.write('                @Param(name="usuario.email",type="string")\n')
                f.write('            })\n')
                f.write('        }\n')
                f.write('    )\n')
                f.write('    public static void save(Long id, Usuario usuario){\n')
                f.write('      \n')
                f.write('      if(id != null){\n')
                f.write('          Usuario usuario_aux = usuario;\n')
                f.write('          usuario = Usuario.findById(id);\n')
                f.write('          if(usuario != null){          \n')
                f.write('	          usuario.nome  = usuario_aux.nome;\n')
                f.write('              usuario.email  = usuario_aux.email;\n')
                f.write('          }else{\n')
                f.write('              //Registro nao encontrado\n')
                f.write('              renderObject(Result.ERROR(3));\n')
                f.write('          }\n')
                f.write('      }\n')
                f.write('      \n')
                f.write('      validation.valid(usuario);\n')
                f.write('      \n')
                f.write('      if (validation.hasErrors()) {\n')
                f.write('          renderObject(Result.VALIDERROR(validation));\n')
                f.write('          return;\n')
                f.write('      }\n')
                f.write('      \n')
                f.write('      Usuario obj_out = usuario.save();\n')
                f.write('      renderObject(Result.OK(obj_out));\n')
                f.write('      \n')
                f.write('    }    \n')
                f.write('}\n')
            finally:
                f.close()
        except IOError:
            pass
        
        print "~ Criando o arquivo controllers/Wadl.java..."
        try:
            f = open("app/controllers/Wadl.java", "w")
            try:
                f.write('package controllers;\n')
                f.write('\n')
                f.write('import utils.Result;\n')
                f.write('import controllers.restapi.DefaultController;\n')
                f.write('import api.wadl.annotation.AnnotationSuport;\n')
                f.write('\n')
                f.write('public class Wadl extends DefaultController {\n')
                f.write('    public static void generate() {\n')
                f.write('        AnnotationSuport.getInstance().addClass(controllers.Usuarios.class);\n')
                f.write('        renderWadl();\n')
                f.write('    }\n')
                f.write('    \n')
                f.write('}\n')
            finally:
                f.close()
        except IOError:
            pass
            
        print "~ Adicionando configuração em conf/application.conf..."
        
        try:
            fo = open("conf/application.conf", "r")
            try:
                string = fo.read()
            finally:
                fo.close()
        except IOError:
            pass
            
        try:
            f = open("conf/application.conf", "w")
            try:
                f.write(string)
                f.write('\n')
                f.write('#Configuração de restapi\n')
                f.write('rest.render=json\n')
                f.write('rest.baseurl=http://localhost:9000/api\n')
            finally:
                f.close()
        except IOError:
            pass
            
        print "~ Adicionando configuração em conf/routes..."
        
        try:
            fo = open("conf/routes", "r")
            try:
                string = fo.read()
            finally:
                fo.close()
        except IOError:
            pass
            
        try:
            f = open("conf/routes", "w")
            try:
                f.write('GET   /						Wadl.generate\n')
                f.write('GET   /api					Wadl.generate\n')
                f.write('GET   /api/wadl				Wadl.generate\n')
                f.write('*     /api/                 module:restapi\n')
                f.write('\n')
                f.write(string)
            finally:
                f.close()
        except IOError:
            pass
            
        print "~ Criando o arquivo conf/result_messages.properties..."
        try:
            f = open("conf/result_messages.properties", "w")
            try:
                f.write('# Default messages\n')
                f.write('# 0=Requisição Realizada com Sucesso\n')
                f.write('# 1=Exceção de Sistema\n')
                f.write('# 2=Exceção de Validação\n')
                f.write('\n')
                f.write('3=Registro não encontrado\n')
                f.write('4=Parametro não informado\n')
                f.write('5=Não foi possível exlcuir\n')
                f.write('6=Não foi possível exlcuir\n')
            finally:
                f.close()
        except IOError:
            pass
        
        print "~ "
        print "~ Arquivos de exemplo gerados com sucesso"
        print "~ "
        print "~ Para testar utilize as URLs:"
        print "~     - http://localhost:9000/api/wadl     => Arquivo WADL"
        print "~     - http://localhost:9000/api/clientes => Obter uma lista de Clientes"
        print ""


# This will be executed before any command (new, run...)
def before(**kargs):
    command = kargs.get("command")
    app = kargs.get("app")
    args = kargs.get("args")
    env = kargs.get("env")


# This will be executed after any command (new, run...)
def after(**kargs):
    command = kargs.get("command")
    app = kargs.get("app")
    args = kargs.get("args")
    env = kargs.get("env")

    if command == "new":
        pass
