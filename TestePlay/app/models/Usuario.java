package models;

import javax.persistence.Entity;
import play.db.jpa.Model;

@Entity
public class Usuario extends Model{

    public String nome;
    public String email;

    @Override
    public String toString(){
        return nome;
    }

}
