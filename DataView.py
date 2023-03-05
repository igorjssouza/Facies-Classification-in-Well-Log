"""
Created on Sat Mar  4 09:33:00 2023

@author: igor
"""
import folium

class DataView():
    
    def __init__(self, df):
        self.df = df
    
    def MarkWellPostionOnMap(self, numWell):
        return self.df[len(self.df)-numWell:len(self.df)]
    
    
    def WellLoc(self):
        mean_lat = self.df['lat'].mean()
        mean_long = self.df['lng'].mean()
        m = folium.Map(location=[mean_lat, mean_long], tiles="OpenStreetMap", zoom_start=7, control_scale=True)
        for index, well_location in self.df.iterrows():
            folium.Marker([well_location['lat'], 
                           well_location['lng']],
                          popup= well_location['SitID']).add_to(m)
        return m
    
    def RenameFeatures(self, feaature_name):
        for i in range(0,len(self.df[feaature_name])):
            self.df[feaature_name][i] = 'well-' + "{}".format(self.df[feaature_name][i])
        
        
        
