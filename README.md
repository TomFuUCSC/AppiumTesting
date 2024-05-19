# hyacinth

Appium w. Python

# Setup

Documentation
* `https://appium.github.io/python-client-sphinx/`
* `https://appium.io/docs/en/2.5/quickstart/`
* `https://www.lambdatest.com/support/docs/appium-python-pytest/`

Directions
1. Following the quickstart documentation, use appium-doctor to correct any misconfiguration issues
2. If you are using VSCode, add python and simcode extensions, otherwise you can use genymotion or real devices
3. Install the necessary drivers for ios and android
4. Use the following configurations (`conftest.py` / `conftest_ios.py`) and set your environment up accordingly
5. Launch appium server
6. Launch the device emulator(s)
7. For android, run the script: `../tests/android/pytest_setup_check.py`(be mindful of the imports from other directories)
8. For ios, run the script: `../tests/ios/pytest_ios_setup.py` (be mindful of the imports from other directories)


Demo Apps
1. For Android, `../apps/android/ApiDemos-debug.apk`
2. For iOS, ``../apps/ios/UIKitCatalog-iphonesimulator.app`
