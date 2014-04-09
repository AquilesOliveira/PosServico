package controllers.restapi;


import play.cache.Cache;
import api.wadl.RestParam;
import api.wadl.RestPath;
import api.wadl.annotation.AnnotationSuport;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import java.util.List;
import java.util.Map;
import play.mvc.Controller;
import utils.Result;
import utils.transform.CustomXStream;
import utils.transform.Exclude;
import utils.transform.JSONExclude;


public class DefaultController extends Controller {

    protected static void renderWadl() {

        AnnotationSuport.getInstance().processWadl();

        Map<String, List<RestPath>> paths = AnnotationSuport.getInstance().getPaths();
        Map<String, RestParam> p_params = AnnotationSuport.getInstance().getParams();
        String ulrbase = AnnotationSuport.getInstance().getUrlBase();

        response.setContentTypeIfNotSet("application/xml");

        renderArgs.put("paths", paths);
        renderArgs.put("p_params", p_params);
        renderArgs.put("ulrbase", ulrbase);
		
		render("wadl.xml");

    }

    protected static void renderObject(int status, Result obj, Exclude exclude) {
        response.status = status;
        if ("XML".equals(play.Play.configuration.getProperty("rest.render").toUpperCase())) {

            CustomXStream xstream;
            if (exclude != null) {
                xstream = new CustomXStream(exclude);
            } else {
                xstream = new CustomXStream(null);
            }
            renderXml(obj, xstream);

        } else {
            if (exclude != null) {
                JSONExclude je = new JSONExclude(exclude.getExclude());
                Gson gson = new GsonBuilder().setExclusionStrategies(je).create();
                renderJSON(gson.toJson(obj));
            } else {
                renderJSON(obj);
            }
        }
    }

    protected static void renderObject(int status, Result obj) {
        renderObject(status, obj, null);
    }

    protected static void renderObject(Result obj) {
        if (obj.getReturn() > 0) {
            renderObject(500, obj, null);
        } else {
            renderObject(200, obj, null);
        }

    }

    protected static void renderObject(Result obj, Exclude exclude) {
        if (obj.getReturn() > 0) {
            renderObject(500, obj, exclude);
        } else {
            renderObject(200, obj, exclude);
        }
    }
	
    public static void routeErro() {
        renderObject(404, Result.SYSERROR("Metodo nao permitido para este recurso"));
    }

}