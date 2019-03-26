package com.example.teste.testedemapa

import android.Manifest.*
import android.annotation.SuppressLint
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.content.pm.PackageManager.*
import android.location.Location
import android.location.LocationListener
import android.location.LocationManager
import android.location.LocationProvider
import android.os.Build
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.provider.Settings
import android.support.v4.app.ActivityCompat
import android.support.v4.app.ActivityCompat.*
import android.util.Log
import android.widget.LinearLayout
import android.widget.Toast
import com.google.android.gms.common.ConnectionResult
import com.google.android.gms.common.api.GoogleApiClient
import com.google.android.gms.maps.*

import com.google.android.gms.maps.model.LatLng
import com.google.android.gms.maps.model.Marker
import com.google.android.gms.maps.model.MarkerOptions
import java.util.jar.Manifest

class MapsActivity : AppCompatActivity(), OnMapReadyCallback{

    private lateinit var mMap: GoogleMap

    lateinit var locationManager: LocationManager
    private var hasGps = false
    private var hasNetwork = false
    private var locationGps: Location? = null

    private var teste123: Location? = null

    private var mapFragment: Any? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_maps)

        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        mapFragment = supportFragmentManager
                .findFragmentById(R.id.map) as SupportMapFragment
        (mapFragment as SupportMapFragment).getMapAsync(this)

    }

    override fun onMapReady(googleMap: GoogleMap) {
        mMap = googleMap

        val listaEnderecos: MutableList<Oficina> = mutableListOf()

        listaEnderecos.add( Oficina("Oficina 1",-23.4761838,-46.7478553, "Descrição da oficina 1") )
        listaEnderecos.add( Oficina("Oficina 2",-23.47546132,-46.7536068, "Descrição da oficina 2") )
        listaEnderecos.add( Oficina("Oficina 3",-23.48208599,-46.75136662, "Descrição da oficina 3") )
        //listaEnderecos.add( Oficina("Oficina 4",-23.48094845,-46.74327707, "Descrição da oficina 4") )

        for (item in listaEnderecos){
            val coordenadas = LatLng(item.lati,item.long)

            var marker: Marker = mMap.addMarker(MarkerOptions().position(coordenadas).title(item.title))
            //marker.setTag(0)
            //mMap.moveCamera(CameraUpdateFactory.newLatLngZoom(coordenadas, 16f))

            var params: Bundle = Bundle()

            params.putString("title", item.title)
            params.putString("info", item.info)

            println("#-#-#-#-#-#- Title: "+item.title+" ; Info: "+item.info)

            mMap!!.setOnMarkerClickListener(object : GoogleMap.OnMarkerClickListener {
                override fun onMarkerClick(marker: Marker): Boolean {
                    //marker.getTag()

                    val intent = Intent(this@MapsActivity, OficinaInfo :: class.java)

                    println("#-#-#-#-#-#- Title: "+item.title+" ; Info: "+item.info)

                    intent.putExtras(params)

                    startActivity(intent)


                    return false
                }
            })

        }

        getLocation()

        if (ActivityCompat.checkSelfPermission(this,
                android.Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED) {
            mMap.isMyLocationEnabled = true
        }

    }

    @SuppressLint("MissingPermission")
    private fun getLocation() {

        locationManager = getSystemService(Context.LOCATION_SERVICE) as LocationManager
        hasGps = locationManager.isProviderEnabled(LocationManager.GPS_PROVIDER)
        hasNetwork = locationManager.isProviderEnabled(LocationManager.NETWORK_PROVIDER)

        if(hasGps || hasNetwork){

            if(hasGps){
                locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER,5000,0F,object : LocationListener{
                    override fun onLocationChanged(p0: Location?) {
                        if(p0!=null){
                            locationGps = p0

                            teste123 = locationGps
                            //println("~~> teste123 : "+teste123)
                        }
                    }

                    override fun onStatusChanged(p0: String?, p1: Int, p2: Bundle?) {

                    }

                    override fun onProviderEnabled(p0: String?) {

                    }

                    override fun onProviderDisabled(p0: String?) {

                    }

                })

            }

        }else{
            startActivity(Intent(Settings.ACTION_LOCATION_SOURCE_SETTINGS))
        }

    }

    private val locationListener: LocationListener = object : LocationListener {
        override fun onLocationChanged(location: Location) {}
        override fun onStatusChanged(provider: String, status: Int, extras: Bundle) {}
        override fun onProviderEnabled(provider: String) {}
        override fun onProviderDisabled(provider: String) {}
    }
}

class Oficina(var title: String, var lati: Double, var long: Double, var info: String) {}




