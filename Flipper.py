{
    "id": "Flipper",
    "name": "Flipper",
    "publisher": "Flipper",
    "appName": "Flipper.app",
    "bundleId": "com.github.Flipper",
    "lastModified": "2021-02-10T02:55:53Z",
    "currentVersion": "v0.73.0",
    "requirements": [
        {
            "name": "Application Bundle ID",
            "operator": "is",
            "value": "com.flipper.mac",
            "type": "recon",
            "and": true
        }
    ],
    "patches": [
        {
            "version": "v0.74.0",
            "releaseDate": "2020-02-04T20:24:33Z",
            "standalone": true,
            "minimumOperatingSystem": "10.9",
            "reboot": false,
            "killApps": [
                {
                    "bundleId": "com.github.Flipper",
                    "appName": "Flipper.app"
                }
            ],
            "components": [
                {
                    "name": "Flipper",
                    "version": "v0.73.0",
                    "criteria": [
                        {
                            "name": "Application Bundle ID",
                            "operator": "is",
                            "value": "com.github.Flipper",
                            "type": "recon",
                            "and": true
                        },
                        {
                            "name": "Application Version",
                            "operator": "is",
                            "value": "v0.74.0",
                            "type": "recon"
                        }
                    ]
                }
            ],
            "capabilities": [
                {
                    "name": "Operating System Version",
                    "operator": "greater than or equal",
                    "value": "10.9",
                    "type": "recon"
                }
            ],
            "dependencies": []
        }
    ],
    "extensionAttributes": []
}
