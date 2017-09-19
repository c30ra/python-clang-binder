//
//  main_header.hpp
//  python_clang_binder
//
//  Created by Luca Carella on 24/06/2017.
//
//

#ifndef main_header_hpp
#define main_header_hpp

#include <test_files/includer.h>

namespace big{

enum my_enum {BEGIN == 0};

class Boo;
class EXPORT Foo : public Boo
{
public:
    Foo();

    ~Foo() = default;
    Foo(const Foo& other) = default;
    Foo(Foo&& other) = default;
    Foo& operator=(const Foo& other) = default;
    Foo& operator=(Foo&& other) = default;

    void setMe();
};

// class QAnimationGroup;
// class QSequentialAnimationGroup;
// class QAnimationDriver;
//
// class QAbstractAnimationPrivate;
// class Q_CORE_EXPORT QAbstractAnimation : public QObject
// {
//     Q_OBJECT
//
//     Q_PROPERTY(State state READ state NOTIFY stateChanged)
//     Q_PROPERTY(int loopCount READ loopCount WRITE setLoopCount)
//     Q_PROPERTY(int currentTime READ currentTime WRITE setCurrentTime)
//     Q_PROPERTY(int currentLoop READ currentLoop NOTIFY currentLoopChanged)
//     Q_PROPERTY(Direction direction READ direction WRITE setDirection NOTIFY directionChanged)
//     Q_PROPERTY(int duration READ duration)
//
// public:
//     enum Direction {
//         Forward,
//         Backward
//     };
//     Q_ENUM(Direction)
//
//     enum State {
//         Stopped,
//         Paused,
//         Running
//     };
//     Q_ENUM(State)
//
//     enum DeletionPolicy {
//         KeepWhenStopped = 0,
//         DeleteWhenStopped
//     };
//
//     QAbstractAnimation(QObject *parent = Q_NULLPTR);
//     virtual ~QAbstractAnimation();
//
//     State state() const;
//
//     QAnimationGroup *group() const;
//
//     Direction direction() const;
//     void setDirection(Direction direction);
//
//     int currentTime() const;
//     int currentLoopTime() const;
//
//     int loopCount() const;
//     void setLoopCount(int loopCount);
//     int currentLoop() const;
//
//     virtual int duration() const = 0;
//     int totalDuration() const;
//
// Q_SIGNALS:
//     void finished();
//     void stateChanged(QAbstractAnimation::State newState, QAbstractAnimation::State oldState);
//     void currentLoopChanged(int currentLoop);
//     void directionChanged(QAbstractAnimation::Direction);
//
// public Q_SLOTS:
//     void start(QAbstractAnimation::DeletionPolicy policy = KeepWhenStopped);
//     void pause();
//     void resume();
//     void setPaused(bool);
//     void stop();
//     void setCurrentTime(int msecs);
//
// protected:
//     QAbstractAnimation(QAbstractAnimationPrivate &dd, QObject *parent = Q_NULLPTR);
//     bool event(QEvent *event) Q_DECL_OVERRIDE;
//
//     virtual void updateCurrentTime(int currentTime) = 0;
//     virtual void updateState(QAbstractAnimation::State newState, QAbstractAnimation::State oldState);
//     virtual void updateDirection(QAbstractAnimation::Direction direction);
//
// private:
//     Q_DISABLE_COPY(QAbstractAnimation)
//     Q_DECLARE_PRIVATE(QAbstractAnimation)
// };
}
#endif /* main_header_hpp */
