
package controllers;

import api.wadl.annotation.Param;
import api.wadl.annotation.Path;
import api.wadl.annotation.Paths;
import api.wadl.annotation.Resource;
import java.util.List;
import models.Usuario;
import utils.Result;
import controllers.restapi.DefaultController;

@Resource(name="usuarios",param={@Param(name="{id}",type="int")})
public class Usuarios extends DefaultController {    
    
    @Path(method="GET",id="getAllUsuario")
    public static void listAll(){
        List<Usuario> usuarios = Usuario.findAll();			
        renderObject(Result.OK(usuarios));
    }
    
    @Path(name="/{id}",method="GET",id="getUsuarioById")
    public static void findId(Long id) {
        if(id != null) {
            Usuario usuario = Usuario.findById(id);
            if(usuario!=null){
		        renderObject(Result.OK(usuario));
            }else{
                //Registro nao encontrado
		        renderObject(Result.ERROR(3));
            }
        }else{
            //Parametro nao informado
	        renderObject(Result.ERROR(4));
        }       
    }
    
    
    @Path(name="/{id}",method="DELETE",id="deleteUsuario")
    public static void delete(Long id) {
        try {
            Usuario usuario = Usuario.findById(id);
            if(usuario!=null){
                usuario.delete();
                renderObject(Result.OK("Usuario apagado com sucesso."));
            }else{
                //Registro nao encontrado
                renderObject(Result.ERROR(3));
            }
        } catch (Exception ex) {
            //Erro de sistema
            renderObject(Result.SYSERROR(ex.getMessage()));
        }
    }
    
    @Paths(
        {
            @Path(method="POST",id="addUsuario" ,param={
                @Param(name="usuario.nome",type="string"),
                @Param(name="usuario.email",type="string")
            }),
            @Path(name="/{id}",id="saveUsuario",method="PUT", param={
                @Param(name="usuario.nome",type="string"),
                @Param(name="usuario.email",type="string")
            })
        }
    )
    public static void save(Long id, Usuario usuario){
      
      if(id != null){
          Usuario usuario_aux = usuario;
          usuario = Usuario.findById(id);
          if(usuario != null){          
	          usuario.nome  = usuario_aux.nome;
              usuario.email  = usuario_aux.email;
          }else{
              //Registro nao encontrado
              renderObject(Result.ERROR(3));
          }
      }
      
      validation.valid(usuario);
      
      if (validation.hasErrors()) {
          renderObject(Result.VALIDERROR(validation));
          return;
      }
      
      Usuario obj_out = usuario.save();
      renderObject(Result.OK(obj_out));
      
    }    
}
