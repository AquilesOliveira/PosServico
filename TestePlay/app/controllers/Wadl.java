package controllers;

import utils.Result;
import controllers.restapi.DefaultController;
import api.wadl.annotation.AnnotationSuport;

public class Wadl extends DefaultController {
    public static void generate() {
        AnnotationSuport.getInstance().addClass(controllers.Usuarios.class);
        AnnotationSuport.getInstance().addClass(controllers.Produtos.class);
        renderWadl();
    }
    
}
