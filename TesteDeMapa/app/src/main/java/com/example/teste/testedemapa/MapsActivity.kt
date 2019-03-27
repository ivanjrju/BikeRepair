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
import com.google.android.gms.maps.model.*

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

        googleMap.setMapStyle(MapStyleOptions.loadRawResourceStyle(this, R.raw.style_json))

        val listaEnderecos: MutableList<Oficina> = mutableListOf()

        listaEnderecos.add( Oficina("Augue",-23.4761838,-46.7478553, "Lorem ipsum hendrerit dictumst quisque, lobortis tristique vivamus.") )
        listaEnderecos.add( Oficina("Massa",-23.47546132,-46.7536068, "Mi blandit condimentum et purus, enim torquent ut.") )
        listaEnderecos.add( Oficina("Hac",-23.48208599,-46.75136662, "Et faucibus vitae nec aenean, viverra justo per.") )
        listaEnderecos.add( Oficina("Aliquam",-23.48094845,-46.74327707, "Fusce lacus praesent ut accumsan, vestibulum tortor sit.") )

        for (item in listaEnderecos){

            val coordenadas = LatLng(item.lati,item.long)
            var marker: Marker = mMap.addMarker(MarkerOptions().position(coordenadas).title(item.title)
                                .icon(BitmapDescriptorFactory.defaultMarker(BitmapDescriptorFactory.HUE_MAGENTA))
                                .alpha(0.9f))
            marker.setTag(item)
            //mMap.moveCamera(CameraUpdateFactory.newLatLngZoom(coordenadas, 16f))

            mMap!!.setOnMarkerClickListener(object : GoogleMap.OnMarkerClickListener {
                override fun onMarkerClick(marker: Marker): Boolean {

                    var oficina : Oficina= marker.getTag() as Oficina
                    val intent = Intent(this@MapsActivity, OficinaInfo :: class.java)

                    var params: Bundle = Bundle()
                    params.putString("title", oficina.title)
                    params.putString("info", oficina.info)

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
/*
private val locationListener: LocationListener = object : LocationListener {
    override fun onLocationChanged(location: Location) {}
    override fun onStatusChanged(provider: String, status: Int, extras: Bundle) {}
    override fun onProviderEnabled(provider: String) {}
    override fun onProviderDisabled(provider: String) {}
}
*/
}

class Oficina(var title: String, var lati: Double, var long: Double, var info: String) {}




