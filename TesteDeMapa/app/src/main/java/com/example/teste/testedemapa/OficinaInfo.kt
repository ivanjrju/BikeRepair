package com.example.teste.testedemapa

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.widget.TextView

class OficinaInfo : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_oficina_info)

        var intent: Intent = getIntent()

        if(intent != null){
            var params: Bundle = intent.getExtras()

            if(params != null){
                var title: String = params.getString("title")
                var info: String = params.getString("info")

                var titleView: TextView = findViewById(R.id.title) as TextView
                var infoView: TextView = findViewById(R.id.info) as TextView

                titleView.setText(title)
                infoView.setText(info)

            }
        }

    }
}
