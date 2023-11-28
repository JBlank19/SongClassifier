Attributes explanation:

https://developer.spotify.com/documentation/web-api/reference/get-audio-features

The key the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1.

Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.

Super_genre is 
he creado una columna super genre que reclasifica los generos en numeros asociados a super generos que he encontrado en https://musicmap.info/.

'Industrial/Gothic': 0,
'EDM': 1,
'Reggae': 2,
'Metal': 3,
'Blues/Jazz': 4,
'Country': 5,
'Urban/Reggaeton': 6,
'Rap/Hiphop': 7,
'Rock/Indie': 8,
'Pop': 9,
'Classical': 10,
'Folk/Traditional': 11,
'Miscellaneous': 12

Se aplica un criterio de priorizar especificidad frente a generos más "paraguas".