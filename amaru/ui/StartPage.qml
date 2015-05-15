import QtQuick 2.0

Rectangle {
    id: root

    color: "#272822";
    signal animationFinished;

    SequentialAnimation {
        id: animation
        running: false

        NumberAnimation { target: text; property: "opacity"; to: 1; from: 0; duration: 1000 }

        onStopped: {
            root.animationFinished();
        }
    }

    Text {
        id: text

        anchors.horizontalCenter: parent.horizontalCenter;
        anchors.verticalCenter: parent.verticalCenter;
        text: qsTr("Welcome to Amaru!");
        color: "#414238";
        font.pointSize: 36;
    }

    Text {
        id: description

        anchors.horizontalCenter: parent.horizontalCenter;
        anchors.verticalCenter: parent.verticalCenter;
        text: qsTr("Welcome to the last version of Amaru.\nIf you run into any problems, report the issue on GitHub.")
        font.pointSize: 22;
        visible: false
        color: "#414238"
    }

    function start_animation() {
        animation.start();
    }
}
